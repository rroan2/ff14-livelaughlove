import privateinfo
import asyncpraw

async def fashionFetch():
    reddit = asyncpraw.Reddit(
    client_id = privateinfo.info.client_id,
    client_secret = privateinfo.info.client_secret,
    username = privateinfo.info.username,
    password = privateinfo.info.password,
    user_agent = "praw",
    )

    user = await reddit.redditor("kaiyoko")
    async for post in user.submissions.top(time_filter="week"):
        if("Fashion Report" in post.title):
            return post
    return ""