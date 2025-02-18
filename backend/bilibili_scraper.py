from bilibili_api import video, favorite_list, sync, Credential
from bilibili_api.favorite_list import FavoriteList

seesdata=""
bili_jct = ""
cre = Credential(seesdata, bili_jct)

async def get_favorite_list():
    # 获取收藏列表
    fav_list = FavoriteList(credential=cre,media_id=89995481)
    resp = await fav_list.get_content()
    print(resp)


sync(get_favorite_list())