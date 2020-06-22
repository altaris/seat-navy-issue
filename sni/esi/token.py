"""
EVE token (access and refresh) management
"""

from typing import Optional

import mongoengine

import sni.esi.sso as sso
import sni.time as time
import sni.uac.user as user


class EsiAccessToken(mongoengine.Document):
    """
    A model representing an ESI access token, along with its refresh token and
    relevant metadatas.
    """
    access_token = mongoengine.StringField(required=True)
    created_on = mongoengine.DateTimeField(required=True, default=time.now)
    expires_on = mongoengine.DateTimeField(required=True)
    owner = mongoengine.ReferenceField(
        user.User, required=True, reverse_delete_rule=mongoengine.DO_NOTHING)
    scopes = mongoengine.ListField(mongoengine.StringField(),
                                   required=True,
                                   default=[])


class EsiRefreshToken(mongoengine.Document):
    """
    A model representing an ESI access token, along with its refresh token and
    relevant metadatas.
    """
    created_on = mongoengine.DateTimeField(required=True, default=time.now)
    updated_on = mongoengine.DateTimeField(required=True, default=time.now)
    owner = mongoengine.ReferenceField(
        user.User, required=True, reverse_delete_rule=mongoengine.DO_NOTHING)
    refresh_token = mongoengine.StringField(required=True)
    scopes = mongoengine.ListField(mongoengine.StringField(),
                                   required=True,
                                   default=[])


def get_access_token(character_id: int,
                     scope: Optional[str]) -> EsiAccessToken:
    """
    Returns an access token, refreshes if needed

    Todo:
        Support multiple scopes.
    """
    owner: user.User = user.User.objects.get(character_id=character_id)
    esi_access_token: EsiAccessToken = EsiAccessToken.objects(
        owner=owner,
        scopes=scope,
        expires_on__gt=time.now(),
    ).first()
    if not esi_access_token:
        esi_refresh_token: EsiRefreshToken = EsiRefreshToken.objects.get(
            owner=owner,
            scopes=scope,
        )
        esi_access_token = save_esi_tokens(
            sso.refresh_access_token(esi_refresh_token.refresh_token))
    return esi_access_token


def save_esi_tokens(
        esi_response: sso.AuthorizationCodeResponse) -> EsiAccessToken:
    """
    Saves the tokens contained in an SSO reponse into the database.

    Create the owner user if necessary.

    Returns:
        The new ESI access token.
    """
    decoded_access_token = sso.decode_access_token(esi_response.access_token)
    owner = user.get_user(decoded_access_token.character_id)
    esi_refresh_token: EsiRefreshToken = EsiRefreshToken.objects(
        owner=owner,
        scopes__all=decoded_access_token.scp,
    ).first()
    if esi_refresh_token:
        esi_refresh_token.refresh_token = esi_response.refresh_token
        esi_refresh_token.updated_on = time.now()
        esi_refresh_token.save()
    else:
        EsiRefreshToken(
            owner=owner,
            refresh_token=esi_response.refresh_token,
            scopes=decoded_access_token.scp,
        ).save()
    return EsiAccessToken(
        access_token=esi_response.access_token,
        expires_on=time.from_timestamp(decoded_access_token.exp),
        owner=owner,
        scopes=decoded_access_token.scp,
    ).save()
