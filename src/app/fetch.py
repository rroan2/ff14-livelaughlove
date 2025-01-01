from privateinfo import info
import asyncpraw

async def fashionFetch():
    reddit = asyncpraw.Reddit(
    client_id = info.client_id,
    client_secret = info.client_secret,
    username = info.username,
    password = info.password,
    user_agent = "praw",
    )

    user = await reddit.redditor("kaiyoko")
    async for post in user.submissions.top(time_filter="week"):
        if("Fashion Report" in post.title):
            return post
    return ""