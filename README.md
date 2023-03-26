# YOUR SPOTIFY MUSIC
#### Video Demo:  https://youtu.be/g8EXZ8kEz4Q
#### Description: 'Your Spotify Music' is a web-app which allows a Spotify to learn more about their listening activity in the past 6 months and understand certain key features of the top artists and tracks they are listening to.

To begin with, I went through the Spotify Web API documentation to understand more about how I can use Spotify's API to integrate with my web application. Out of the many methods available for OAuth with the API, I decided to go with the [Authorization code flow](https://developer.spotify.com/documentation/general/guides/authorization/code-flow/) method as it serves my use case of each user being able to allow each user to see more about their tracks.

Once I had done the integration I used Python to deduce some statistics from the song data that I was receiving through the API.
The statistics I pulled were as follows:
1. *Valence*: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric)
2. *Danceability*: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
3. *Instrumentalness* : Predicts whether a track contains no vocals.The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content.
4. *Key signature*: The key the track is in.
5. *Genre* : This describes the genre of the artist. Please note that Spotify gives genre only at an artist level and not at the song track level.

**Obtaining details via APIs:**
The [Spotify Developers Console](https://developer.spotify.com/console/) is a great place to check out all the endpoints with their usage. it also gives a sample of the response that you shall receive by entering some dummy inputs. I obtained the following details via the Spotify Web API endpoints:
1. *User details*: I wanted to personalize the intro of the webpage with the name of the user. I used the following endpoint: /v1/users/{user_id} under the 'User's Profile' section.
2. *Track features*: I wanted to pull in the top tracks and artists for the user and basis that info, I wanted to compute certain key metrics of the songs that the user has been listening to in the past 6 months. So this can be divided into 2 parts:
a) Get the top tracks and artists for the user
b) Basis audio features of each top track/artist fetched, return a statistical value (mean, median etc.) to the user.
**Top tracks and artists:**
The API endpoint for this is [/v1/me/top/{type}](https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/). To obtain top tracks, one simply enters tracks as the query parameters - /v1/me/top/tracks. To obtain top artists, enter artists as the query parameters- v1/me/top/type/artists. You can find more details on the detailed documentation [here](https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/)

**Audio features:**
The API endpoint to obtain audio features is [/v1/audio-features/{id}](https://api.spotify.com/v1/audio-features/{id}). Spotify gives a number of audio features computed for each track in its database. For the purpose of my app, I used valence, danceability, instrumentalness and key signature. You can choose any of the others. You can find more about it [here](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features)
I also decided to pull in the images of top tracks and top artists so that users can see what they have been listening to most in the past 6 months.

**Designing the front-end UI:**
Designing the front-end UI was much harder than I previously thought thanks to the fact that I hadn't extensively used Bootstrap before. Bootstrap is a framework which allows one to build mobile responsive websites. Their latest version is 5.2, so make sure you are reading the documentation for the latest version whenever you have queries.

After spending some time understanding the concept of containers, navbar, col-md etc I was able to design the UI of my website using Bootstrap. 
Apart from the documentation, the following video helped  expedite my understanding of Bootstrap 5:
[Video](https://youtu.be/4sosXZsdy-s) - very useful resource where the creator goes through the step by step process of designing the UI of website and in the process includes many features of Bootstrap

Next steps:
While making this app, I attempted to build a word cloud of the artists' genres that the user is listening to. However, I ran into issues due to multi-threading. As next steps I plan to include that as well and make the application more interactive so that users can play around and explore songs of their own liking.

