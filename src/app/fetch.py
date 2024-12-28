import asyncpraw

async def fashionFetch():
    reddit = asyncpraw.Reddit(
    client_id = "client_id",
    client_secret = "client_secret",
    username = "username",
    password = "password",
    user_agent = "praw",
    )

    user = await reddit.redditor("kaiyoko")
    async for post in user.submissions.top(time_filter="week"):
        if("Fashion Report" in post.title):
            return post
    return ""