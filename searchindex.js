Search.setIndex({docnames:["apiserver","authentication","configuration","database","esi","index","openapi","sni","todos","uac","users"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":1,"sphinx.domains.index":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.todo":2,"sphinx.ext.viewcode":1,sphinx:56},filenames:["apiserver.rst","authentication.rst","configuration.rst","database.rst","esi.rst","index.rst","openapi.rst","sni.rst","todos.rst","uac.rst","users.rst"],objects:{"sni.__main__":{main:[7,1,1,""],parse_command_line_arguments:[7,1,1,""],print_openapi_spec:[7,1,1,""],start_api_server:[7,1,1,""]},"sni.apiserver":{does_not_exist_exception_handler:[0,1,1,""],exception_handler:[0,1,1,""],get_ping:[0,1,1,""]},"sni.conf":{assert_is_set:[2,1,1,""],flatten_dict:[2,1,1,""],get:[2,1,1,""],load_configuration_file:[2,1,1,""]},"sni.db":{init:[3,1,1,""],migrate:[3,1,1,""],migrate_ensure_root:[3,1,1,""],migrate_ensure_root_dyn_token:[3,1,1,""],migrate_ensure_root_per_token:[3,1,1,""]},"sni.dbmodels":{EsiToken:[3,2,1,""],StateCode:[3,2,1,""],Token:[3,2,1,""],User:[3,2,1,""]},"sni.dbmodels.EsiToken":{DoesNotExist:[3,3,1,""],MultipleObjectsReturned:[3,3,1,""],__objects:[3,4,1,""],_cached_reference_fields:[3,4,1,""],_class_name:[3,4,1,""],_collection:[3,4,1,""],_db_field_map:[3,4,1,""],_fields:[3,4,1,""],_fields_ordered:[3,4,1,""],_is_base_cls:[3,4,1,""],_is_document:[3,4,1,""],_meta:[3,4,1,""],_reverse_db_field_map:[3,4,1,""],_subclasses:[3,4,1,""],_superclasses:[3,4,1,""],_types:[3,4,1,""],access_token:[3,4,1,""],app_token:[3,4,1,""],created_on:[3,4,1,""],expires_on:[3,4,1,""],id:[3,4,1,""],objects:[3,4,1,""],owner:[3,4,1,""],refresh_token:[3,4,1,""],scopes:[3,4,1,""]},"sni.dbmodels.StateCode":{DoesNotExist:[3,3,1,""],MultipleObjectsReturned:[3,3,1,""],__objects:[3,4,1,""],_cached_reference_fields:[3,4,1,""],_class_name:[3,4,1,""],_collection:[3,4,1,""],_db_field_map:[3,4,1,""],_fields:[3,4,1,""],_fields_ordered:[3,4,1,""],_is_base_cls:[3,4,1,""],_is_document:[3,4,1,""],_meta:[3,4,1,""],_reverse_db_field_map:[3,4,1,""],_subclasses:[3,4,1,""],_superclasses:[3,4,1,""],_types:[3,4,1,""],app_token:[3,4,1,""],created_on:[3,4,1,""],id:[3,4,1,""],objects:[3,4,1,""],uuid:[3,4,1,""]},"sni.dbmodels.Token":{DoesNotExist:[3,3,1,""],MultipleObjectsReturned:[3,3,1,""],TokenType:[3,2,1,""],__objects:[3,4,1,""],_cached_reference_fields:[3,4,1,""],_class_name:[3,4,1,""],_collection:[3,4,1,""],_db_field_map:[3,4,1,""],_fields:[3,4,1,""],_fields_ordered:[3,4,1,""],_is_base_cls:[3,4,1,""],_is_document:[3,4,1,""],_meta:[3,4,1,""],_reverse_db_field_map:[3,4,1,""],_subclasses:[3,4,1,""],_superclasses:[3,4,1,""],_types:[3,4,1,""],callback:[3,4,1,""],comments:[3,4,1,""],created_on:[3,4,1,""],expires_on:[3,4,1,""],id:[3,4,1,""],objects:[3,4,1,""],owner:[3,4,1,""],parent:[3,4,1,""],token_type:[3,4,1,""],uuid:[3,4,1,""]},"sni.dbmodels.Token.TokenType":{_generate_next_value_:[3,5,1,""],_member_map_:[3,4,1,""],_member_names_:[3,4,1,""],_member_type_:[3,4,1,""],_value2member_map_:[3,4,1,""],dyn:[3,4,1,""],per:[3,4,1,""],use:[3,4,1,""]},"sni.dbmodels.User":{DoesNotExist:[3,3,1,""],MultipleObjectsReturned:[3,3,1,""],__objects:[3,4,1,""],_cached_reference_fields:[3,4,1,""],_class_name:[3,4,1,""],_collection:[3,4,1,""],_db_field_map:[3,4,1,""],_fields:[3,4,1,""],_fields_ordered:[3,4,1,""],_is_base_cls:[3,4,1,""],_is_document:[3,4,1,""],_meta:[3,4,1,""],_reverse_db_field_map:[3,4,1,""],_subclasses:[3,4,1,""],_superclasses:[3,4,1,""],_types:[3,4,1,""],character_id:[3,4,1,""],character_name:[3,4,1,""],created_on:[3,4,1,""],id:[3,4,1,""],objects:[3,4,1,""],subcharacter_ids:[3,4,1,""]},"sni.esi":{AuthorizationCodeResponse:[4,2,1,""],DecodedAccessToken:[4,2,1,""],decode_access_token:[4,1,1,""],get_access_token:[4,1,1,""],get_auth_url:[4,1,1,""],get_basic_authorization_code:[4,1,1,""],refresh_access_token:[4,1,1,""]},"sni.esi.AuthorizationCodeResponse":{_abc_impl:[4,4,1,""],access_token:[4,4,1,""],expires_in:[4,4,1,""],refresh_token:[4,4,1,""],token_type:[4,4,1,""]},"sni.esi.DecodedAccessToken":{_abc_impl:[4,4,1,""],azp:[4,4,1,""],character_id:[4,5,1,""],exp:[4,4,1,""],iss:[4,4,1,""],jti:[4,4,1,""],kid:[4,4,1,""],name:[4,4,1,""],owner:[4,4,1,""],scp:[4,4,1,""],sub:[4,4,1,""]},"sni.routers":{esi:[0,0,0,"-"],token:[0,0,0,"-"]},"sni.routers.esi":{EsiRequestIn:[0,2,1,""],PostCallbackEsiOut:[0,2,1,""],get_callback_esi:[0,1,1,""],get_esi_latest:[0,1,1,""]},"sni.routers.esi.EsiRequestIn":{_abc_impl:[0,4,1,""],on_behalf_of:[0,4,1,""],params:[0,4,1,""]},"sni.routers.esi.PostCallbackEsiOut":{_abc_impl:[0,4,1,""],state_code:[0,4,1,""],user_token:[0,4,1,""]},"sni.routers.token":{GetTokenOut:[0,2,1,""],PostTokenDynIn:[0,2,1,""],PostTokenDynOut:[0,2,1,""],PostTokenPerIn:[0,2,1,""],PostTokenPerOut:[0,2,1,""],PostTokenUseFromDynIn:[0,2,1,""],PostTokenUseFromDynOut:[0,2,1,""],PostUseFromPerOut:[0,2,1,""],delete_token:[0,1,1,""],get_token:[0,1,1,""],post_token_dyn:[0,1,1,""],post_token_per:[0,1,1,""],post_token_use_from_dyn:[0,1,1,""],post_token_use_from_per:[0,1,1,""]},"sni.routers.token.GetTokenOut":{_abc_impl:[0,4,1,""],callback:[0,4,1,""],comments:[0,4,1,""],created_on:[0,4,1,""],expires_on:[0,4,1,""],owner_character_id:[0,4,1,""],parent:[0,4,1,""],token_type:[0,4,1,""],uuid:[0,4,1,""]},"sni.routers.token.PostTokenDynIn":{_abc_impl:[0,4,1,""],callback:[0,4,1,""],comments:[0,4,1,""]},"sni.routers.token.PostTokenDynOut":{_abc_impl:[0,4,1,""],app_token:[0,4,1,""]},"sni.routers.token.PostTokenPerIn":{_abc_impl:[0,4,1,""],callback:[0,4,1,""],comments:[0,4,1,""]},"sni.routers.token.PostTokenPerOut":{_abc_impl:[0,4,1,""],app_token:[0,4,1,""]},"sni.routers.token.PostTokenUseFromDynIn":{_abc_impl:[0,4,1,""],scopes:[0,4,1,""]},"sni.routers.token.PostTokenUseFromDynOut":{_abc_impl:[0,4,1,""],login_url:[0,4,1,""],state_code:[0,4,1,""]},"sni.routers.token.PostUseFromPerOut":{_abc_impl:[0,4,1,""],user_token:[0,4,1,""]},sni:{__main__:[7,0,0,"-"],apiserver:[0,0,0,"-"],conf:[2,0,0,"-"],db:[3,0,0,"-"],dbmodels:[3,0,0,"-"],esi:[4,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","function","Python function"],"2":["py","class","Python class"],"3":["py","exception","Python exception"],"4":["py","attribute","Python attribute"],"5":["py","method","Python method"]},objtypes:{"0":"py:module","1":"py:function","2":"py:class","3":"py:exception","4":"py:attribute","5":"py:method"},terms:{"24h":1,"299bd5a9f432a7b9a584e91801cb95a3":2,"2c48822e0a1b":4,"3f961d92a82060c4375de5683e1a7f4d94bd48e3ba861c49a40708e3c9976ea1":2,"43c5":4,"48h":1,"702e1947f7b876e73b790cbc1f13c9ad8a3b94e6":2,"8pmzcetkb4vfudrhlc":4,"998e12c7":4,"abstract":3,"catch":0,"class":[0,2,3,4],"default":[2,3,4],"enum":3,"function":3,"int":[0,4],"new":[0,3],"null":3,"return":[0,3,4],"short":3,"true":[2,3],"try":3,"while":3,EVE:[0,2,3,4,5],For:9,The:[2,3,4,5,8],Then:5,There:1,Use:3,Uses:3,__main__:7,__object:3,_abc_data:[0,4],_abc_impl:[0,4],_cached_reference_field:3,_cl:3,_class_nam:3,_collect:3,_db_field_map:3,_field:3,_fields_ord:3,_generate_next_value_:3,_id:3,_is_base_cl:3,_is_docu:3,_member_map_:3,_member_names_:3,_member_type_:3,_meta:3,_request:0,_reverse_db_field_map:3,_subclass:3,_superclass:3,_type:3,_value2member_map_:3,about:[0,3],abov:9,accept:3,access:[3,4,5],access_token:[3,4],accur:3,act:3,action:9,actor:9,actual:9,add:3,added:3,admin:2,aezxdswm:4,affili:5,after:[1,3],against:9,algorithm:2,alia:3,all:[0,5,9],allianc:[4,9],allow:3,allow_inherit:3,along:[3,4],alreadi:3,also:[1,2],altari:5,altern:3,ani:[2,3],anyhttpurl:0,anyth:3,api:[1,2,5,7,9],apimodel:[0,1],apiserv:0,app:[0,1,2,3,5],app_token:[0,3],applic:[0,1,2,4,5],arg:3,argpars:7,argument:[3,4,7],around:3,asctim:2,assert_is_set:2,asset:[4,9],associ:3,async:0,authdynout:1,authent:[0,3,5],authentication_sourc:2,author:[1,4],authorizationcoderespons:4,authperout:1,automat:3,avail:3,azp:4,base:[0,3,4],basemodel:[0,4],bash:5,bearer:[1,4],becaus:3,befor:3,being:0,bit:3,bloke:4,bookmark:4,broken:3,builtin:3,c_a:2,c_b_x:2,c_b_y:2,calendar:4,call:[0,3],callback:[0,3,5],can:[0,1,3,9],cannot:3,cascad:3,certain:9,chang:[3,5],charact:[3,4,9],character_id:[3,4,9],character_nam:3,characterstat:4,chr:9,client_id:[2,4],client_secret:[2,4],clone:4,coa:9,coalit:9,code:[0,3,4,5],collect:3,com:[2,4,5],command:7,comment:[0,3],complexdatetimefield:3,compos:5,compris:9,conf:2,config:2,configur:5,connect:3,consid:3,contain:[3,5,7],container_nam:5,contract:4,control:5,convert:[3,4],corpor:[4,9],correspond:3,count:3,creat:[0,2,3,5],created_on:[0,3],createus:5,credit:2,crp:9,current:[0,3],custom:3,data:[0,5],databas:[2,5,9],date:3,datetim:[0,3],datetimefield:3,dateutil:3,dbmodel:[0,3],debug:2,decod:4,decode_access_token:4,decodedaccesstoken:4,delet:[0,3],delete_rul:3,delete_token:0,deni:3,depend:[0,3],derefer:3,dereferenc:3,deriv:[1,4],develop:[2,5],dict:[0,2],dictfield:3,dictionnari:2,direct:3,disable_existing_logg:2,do_noth:3,doc:4,docker:5,docstr:8,document:[3,7],doe:[2,3],does_not_exist_exception_handl:0,doesnotexist:[0,3],domain:5,don:[3,5],done:[0,1],dyn:[0,3],dynam:[0,1,3],easiest:5,effect:3,either:9,embeddeddocu:3,empti:3,end:3,endpoint:9,entiti:9,entri:[7,8],enumer:3,environ:5,error:[0,3],esi:[1,2,3,5,8,9],esi_path:0,esi_scop:4,esi_token:3,esirequestin:0,esitoken:3,especi:3,eveonlin:4,everytim:3,evetech:4,exampl:[5,9],except:[0,2,3],exception_handl:0,exec:5,exist:3,exp:4,expir:1,expires_in:4,expires_on:[0,3],ext:2,extend:3,extra:3,extract:4,facil:5,fals:[2,3],featur:3,field:[3,4],file:[2,5],first:3,fit:4,flatten:2,flatten_dict:2,fleet:4,follow:[5,9],forget:5,form:[1,4],format:[2,3],formatt:2,forward:0,from:[0,1,2,3,4],fulli:3,gener:2,get:[0,1,2,3,4],get_access_token:[4,8],get_auth_url:4,get_basic_authorization_cod:4,get_callback_esi:0,get_esi_latest:0,get_p:0,get_token:0,gettokenout:0,git:5,git_url:5,github:[5,8],global:0,group:9,grp:9,handl:3,handler:[0,2],happen:3,have:2,header:1,here:2,hex:2,host:2,hs256:2,html:4,http:[2,4,5],id_field:3,imag:5,immedi:3,implement:3,imran:2,inact:1,includ:1,index:[3,5],index_background:3,index_opt:3,index_spec:3,industri:4,info:2,inform:0,inherit:1,init:3,initi:3,input:3,instal:3,instanc:3,integ:3,intfield:3,invaliddocumenterror:3,iss:4,issu:[0,3,4,9],its:[3,4],job:3,jti:4,jwt:[1,2,4,8],jzozkrta8b:4,kei:[2,4],kid:4,killmail:4,kind:1,known:3,last_valu:3,layer:5,lazili:3,lazyreferencefield:3,lead:3,level:2,levelnam:2,librari:3,like:4,line:[7,8],list:[0,3,4,5],listfield:3,load:2,load_configuration_fil:2,localhost:2,locat:[2,4,8],log:[1,2,3],logger:2,login:4,login_url:0,look:4,lqjg2:4,magic:3,mail:4,main:[4,5],manag:[0,3,5,9],manage_planet:4,mani:3,manual:1,mapfield:3,market:4,match:5,max_docu:3,max_siz:3,mean:[3,9],messag:2,metadata:3,method:3,microsecond:3,migrat:3,migrate_ensure_root:3,migrate_ensure_root_dyn_token:3,migrate_ensure_root_per_token:3,millisecond:3,mode:2,model:[0,1,5],modifi:3,mongo:5,mongo_initdb_root_password:5,mongo_initdb_root_usernam:5,mongodb:[3,5],mongoengin:[0,3],more:4,multipl:3,multipleobjectsreturn:3,must:[0,1,3],mutablemap:2,my3rdpartyclientid:4,name:[2,4,9],namespac:7,nearest:3,necessari:3,need:3,nested_dict:2,net:4,none:[0,2,3,4,7],note:[1,3],notif:0,notifi:0,nullifi:3,oauth:[0,4],object:[0,3,4],objectid:3,objectidfield:3,on_behalf_of:0,onc:0,one:3,onli:3,open_window:4,openapi:[5,7],openssl:2,option:[0,3],order:[1,3],org:3,organize_mail:4,origin:[5,8],other:[0,3],own:3,owner:[0,3,4],owner_character_id:0,page:5,param:0,paramet:4,parent:[0,3],parent_kei:2,pars:[3,7],parse_command_line_argu:7,parser:3,pass:[3,4],password:[2,5],path:[0,2],per:[0,3],perform:[3,9],perman:[0,1,3],planet:4,point:7,pong:0,poor:3,port:2,portal:[2,5],post:0,post_token_dyn:0,post_token_p:0,post_token_use_from_dyn:0,post_token_use_from_p:0,postcallbackesiout:0,posttokendynin:0,posttokendynout:0,posttokenperin:0,posttokenperout:0,posttokenusefromdynin:0,posttokenusefromdynout:0,postusefromperout:0,pre:3,precis:[3,4],predefin:0,present:3,prevent:3,print:[0,7],print_openapi_spec:7,privileg:1,probabl:3,propag:2,properti:4,proxi:9,publicdata:4,pull:3,pumba:5,pwd:5,pydant:[0,4],pyjwt:2,python:3,python_main:5,queryset:3,rais:[2,3],rand:2,read:4,read_agents_research:4,read_asset:4,read_blueprint:4,read_calendar_ev:4,read_character_bookmark:4,read_character_contract:4,read_character_job:4,read_character_min:4,read_character_ord:4,read_character_wallet:4,read_chat_channel:4,read_clon:4,read_contact:4,read_container_log:4,read_corporation_asset:4,read_corporation_bookmark:4,read_corporation_contract:4,read_corporation_job:4,read_corporation_killmail:4,read_corporation_membership:4,read_corporation_min:4,read_corporation_ord:4,read_corporation_rol:4,read_corporation_wallet:4,read_customs_offic:4,read_divis:4,read_facil:4,read_fatigu:4,read_fit:4,read_fleet:4,read_fw_stat:4,read_impl:4,read_killmail:4,read_loc:4,read_loyalti:4,read_mail:4,read_med:4,read_notif:4,read_onlin:4,read_opportun:4,read_ship_typ:4,read_skil:4,read_skillqueu:4,read_stand:4,read_starbas:4,read_structur:4,read_titl:4,readwrit:5,receiv:0,redi:[2,5],refer:[0,3,4,5,9],referenc:3,referencefield:3,refresh:[3,4],refresh_access_token:4,refresh_token:[3,4],regist:[3,5],register_delete_rul:3,relat:[0,3],relev:[3,9],remeb:3,repons:[0,4],repres:[3,9],request:[0,1,5,9],requir:[1,3,5],respond_calendar_ev:4,respons:[0,1,4],retriev:3,reverse_delete_rul:3,revok:1,rguc:4,role:5,root:[1,2,3,5],root_url:2,rootpassword:5,round:3,router:5,rule:3,run:[3,7],same:3,scope:[0,3,5,9],scp:4,search:[4,5],search_structur:4,second:3,secret:2,see:[1,2,3,5,9],send_mail:4,separ:[2,9],server:[2,5,7],servic:5,set:[2,3],shell:5,should:[3,4],signatur:4,singl:3,skill:4,sni:[0,1,2,3,4,7,8],snipassword:[2,5],solv:3,some:[3,4],sourc:[0,2,3,4,7],spars:3,specif:[5,7],src:5,sso:[0,1,3,4],standard:[2,3],start:3,start_api_serv:7,state:[0,3,4],state_cod:[0,3],statecod:3,stdout:2,store:9,str:[0,2,3,4],stream:2,streamhandl:2,string:[3,4,9],stringfield:3,strptime:3,structure_market:4,sub:[3,4],subcharacter_id:3,support:[2,3],syntax:3,sys:2,tabl:9,take:1,talk:4,them:0,themselv:1,thi:[1,3,4,7,9],tied:[0,1],time:3,todo:5,token:[1,3,4,5,8],token_typ:[0,3,4],tokentyp:[0,3],trace:0,track_memb:4,tupl:9,two:1,type:[3,9],under:1,unicod:3,uniqu:3,univers:4,updat:3,url:[0,2,3,4],urlfield:3,urlsafe_b64encod:4,use:[0,1,3,5],used:[0,3],useful:3,user:[0,1,3,5],user_token:0,usernam:[2,5],using:[0,3,9],usr:5,utc:3,utcnow:3,utilis:3,uuid:[0,3],uuidfield:3,valid:[1,3,4,8],validate_head:0,valu:[2,3],vari:3,variou:3,version:[2,3,5],via:1,volum:5,wai:[3,5],wallet:4,web:[0,4],web_based_sso_flow:4,what:3,when:[0,3],where:9,which:[0,1,2,3,9],whose:9,wish:[1,9],within:9,workspac:8,wrap:3,wrapper:3,write_contact:4,write_fit:4,write_fleet:4,write_waypoint:4,yaml:[2,7],yml:[2,5],you:3,your:5},titles:["API Server","Authentication","Configuration facility","Database layer","ESI requests layer","SeAT Navy Issue","OpenAPI specification","Main module","Todo list","User Access Control","User management"],titleterms:{access:9,api:0,authent:1,configur:2,control:9,databas:3,document:[2,4,5],esi:[0,4],exampl:2,facil:2,high:5,indic:5,issu:5,layer:[3,4],level:5,list:8,main:[0,7],manag:10,model:3,modul:[0,2,4,5,7],navi:5,openapi:6,refer:2,request:4,router:0,run:5,scope:4,seat:5,server:0,sni:5,specif:6,tabl:5,todo:[4,8],token:0,user:[9,10]}})