from scrape_title_and_content import scrape_subreddit_content


subreddit = input('Enter Subreddit: ')
posts = int(input('Enter number of posts: '))
comments = int(input('Enter number of comments on post: '))

scrape_subreddit_content(subreddit, posts, comments)