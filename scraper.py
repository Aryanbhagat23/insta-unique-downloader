import instaloader

# We create one instance of the loader to use throughout the app
L = instaloader.Instaloader()

def fetch_insta_data(url_or_username):
    """
    This function detects if the user provided a URL (for Reels/Photos)
    or a Username (for DP download).
    """
    try:
        # Check if it's a profile username (doesn't contain slashes)
        if "/" not in url_or_username:
            profile = instaloader.Profile.from_username(L.context, url_or_username)
            return {
                "type": "DP",
                "username": profile.username,
                "display_url": profile.profile_pic_url, # High-res DP link
                "bio": profile.biography,
                "followers": profile.followers
            }
        
        # Otherwise, treat it as a Post/Reel URL
        # Extract the shortcode (the unique ID in the URL)
        shortcode = url_or_username.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        return {
            "type": "Post/Reel",
            "media_url": post.video_url if post.is_video else post.url,
            "caption": post.caption,
            "thumbnail": post.url,
            "is_video": post.is_video
        }

    except Exception as e:
        return {"error": str(e)}

# Quick test (Uncomment the line below to test it by running: python scraper.py)
# print(fetch_insta_data("https://www.instagram.com/p/C_YourTestShortcode/"))