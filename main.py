import time
import configparser
from random import randint as rint
from DrissionPage import ChromiumPage
from DrissionPage.common import By


def title_matches_all(title, keys):
    if keys == []:
        return True
    for key in keys:
        if key not in title:
            return False
        
    return True

def title_matches_any(title, keys):
    if keys == []:
        return True
    for key in keys:
        if key in title:
            return True
        
    return False

# 窗口最大化 + 调节至50%大小
def adjust_screen(page: ChromiumPage):
    page.set.window.max()
    # w, h = page.rect.viewport_size
    # page.run_cdp('Emulation.setDeviceMetricsOverride',
    #          width=w, height=h,
    #          deviceScaleFactor=1, mobile=False,
    #          scale=0.5)
    input("-请Ctrl- 调整屏幕后回车-")
    return

def match_all_visible_posts(p_keys, s_keys):
    print("等待帖子加载中")
    time.sleep(8)
    print("抓取当前可视的帖子中...")
    hrefs = page.eles((By.CSS_SELECTOR, ".cover.ld.mask")) # 帖子详情页链接
    titles = page.eles((By.CSS_SELECTOR, ".title")) # 帖子标题

    res = []
    for href, title in zip(hrefs, titles):
        link = href.attr('href')
        t = title.text
        print("匹配中的帖子：", t)
        if (title_matches_all(t, p_keys) and title_matches_any(t, s_keys)):
            res.extend(link.split(','))
            print("匹配通过")
        else:
            print("匹配失败")
        time.sleep(1)

    return res


def comment_all_posts(posts, comment):
    sums = 0
    for link in posts:
        sums = sums + 1
        print("序号：", sums, "链接：", link)
        # 访问操作
        page.get(link)
        time.sleep(rint(1,2))
        # 选中文本框操作
        page.ele('.chat-wrapper').click()
        time.sleep(rint(1,3))
        # 填入评论操作
        page.ele('.content-input').input(comment)
        time.sleep(rint(2,3))
        # 提交评论操作
        page.ele('.btn submit').click()
        print("发送成功：", comment)
        time.sleep(rint(3,4))
    return



config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")
page = ChromiumPage()

page.get("https://www.xiaohongshu.com/login")
input("扫码并确认登录后按回车继续...")

P_KEYS = config["configs"]["primary_match"].split('-')
S_KEYS = config["configs"]["secondary_match"].split('-')
COMMENT = config["configs"]["comment_content"]
print(P_KEYS)
print(S_KEYS)
print(COMMENT)
input("确认即将发布的评论内容与匹配词，无误回车运行脚本↵")

# 调整屏幕至合适大小
adjust_screen(page)

# 访问“旅行”推送页面
# 现在是食物
page.get("https://www.xiaohongshu.com/explore")
print("网页加载成功！")

# 循环：评论->刷新
while True:
    posts = match_all_visible_posts(P_KEYS, S_KEYS)
    # posts为所有标题符合匹配条件的帖子
    # 评论所有帖子
    comment_all_posts(posts, COMMENT)
    # 延迟
    time.sleep(rint(2,4))
    # 回到推荐页
    page.get("https://www.xiaohongshu.com/explore?channel_id=homefeed.food_v3")
    print("网页加载成功！")
    # 延迟
    time.sleep(rint(2,3))


#------------------------------------以下部分忽略-------------------------------------------------

# print("开始抓取页面的元素链接！")


# # 获取所有笔记标题和详情页链接
# my_list = list()
# ele = page.eles((By.CSS_SELECTOR, ".cover.ld.mask")) # 一片笔记的详情页链接
# name_ele = page.eles((By.CSS_SELECTOR, ".title"))

# for href, name in zip(ele, name_ele):
#     lian = href.attr('href')
#     na = name.text
#     print("已抓取: ", na, lian)
#     my_list.extend(lian.split(','))


# print("所有抓取的链接（列表）：", my_list)

# # 评论功能
# sums = 0
# for link in my_list:
#     sums = sums + 1
#     print("序号：", sums, "链接：", link)
#     page.get(link)
#     time.sleep(1)
#     input_list1 = page.ele('.chat-wrapper').click()
#     input_list2 = page.ele('.content-input').input(comment)
#     time.sleep(1)
#     button = page.ele('.btn submit').click()
#     print("发送成功：", comment)
#     time.sleep(2)

# print("*" * 30)
# page.quit()
# time.sleep(5)
# input("主程序结束...")
