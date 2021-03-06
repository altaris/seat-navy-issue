"""
User (aka character), corporation, and alliance management
"""

from sni.esi.esi import esi_get

from .models import (
    Alliance,
    Corporation,
    Group,
    User,
)


def ensure_alliance(alliance_id: int) -> Alliance:
    """
    Ensures that an alliance exists, and returns it. It it does not, creates
    it by fetching relevant data from the ESI.
    """
    alliance: Alliance = Alliance.objects(alliance_id=alliance_id).first()
    if alliance is None:
        data = esi_get(f"latest/alliances/{alliance_id}").data
        alliance = Alliance(
            alliance_id=alliance_id,
            alliance_name=str(data["name"]),
            executor_corporation_id=int(data["executor_corporation_id"]),
            ticker=str(data["ticker"]),
        ).save()
        ensure_corporation(alliance.executor_corporation_id)
    return alliance


def ensure_autogroup(name: str) -> Group:
    """
    Ensured that an automatically created group exists. Automatic groups are
    owned by root.
    """
    grp = Group.objects(group_name=name).first()
    if grp is None:
        grp = Group(is_autogroup=True, group_name=name).save()
    return grp


def ensure_corporation(corporation_id: int) -> Corporation:
    """
    Ensures that a corporation exists, and returns it. It it does not, creates
    it by fetching relevant data from the ESI.
    """
    corporation: Corporation = Corporation.objects(
        corporation_id=corporation_id
    ).first()
    if corporation is None:
        data = esi_get(f"latest/corporations/{corporation_id}").data
        alliance = (
            ensure_alliance(int(data["alliance_id"]))
            if "alliance_id" in data
            else None
        )
        corporation = Corporation(
            alliance=alliance,
            ceo_character_id=int(data["ceo_id"]),
            corporation_id=corporation_id,
            corporation_name=str(data["name"]),
            ticker=str(data["ticker"]),
        ).save()
        ensure_user(corporation.ceo_character_id)
    return corporation


def ensure_user(character_id: int) -> User:
    """
    Ensures that a user (with a valid ESI character ID) exists, and returns it.
    It it does not, creates it by fetching relevant data from the ESI. Also
    creates the character's corporation and alliance (if applicable).
    """
    usr = User.objects(character_id=character_id).first()
    if usr is None:
        data = esi_get(f"latest/characters/{character_id}").data
        usr = User(
            character_id=character_id,
            character_name=str(data["name"]),
            corporation=ensure_corporation(int(data["corporation_id"])),
        ).save()
    return usr
