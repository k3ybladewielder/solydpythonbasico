#####TESTE####
from twitter import Twitter

consumer_key = "zlK0HunVHgJIM2G16R4fBNYR4"
consumer_secret = "yyDmK7ntok46jjRpDDAUxIJiiItrs4n9HYNLc6ueTdc0ftAviN"
access_token = "263301347-AgPOYAPZVQxzbACn9NipQfZL103oplTpg4gwN43f"
access_token_secret = "vB8Vcsfjc1rIyPAo5nnjFqs6P46WZOVe03kJ3tGQwXoOz"


twitter = Twitter(consumer_key, consumer_secret, access_token, access_token_secret)

pesq = twitter.pesquisar("titans", "pt")

for resultado in pesq:
    print(resultado["text"])