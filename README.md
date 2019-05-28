# MyCine: Movie Rating System

# Celeb Model
## Common for Actors and Directors

/celeb: Post to add new data

/celeb/id: Get details of a celeb, update using put, delete

```javascript
{
"name": "Celeb Name",
"birth_date": "YYYY-MM-DD"
}
```

Put can update using Partial Data(Cannot change id)

/celeb/director/id: Get Detail of a particular director. Only availabe if Celeb has directed a movie.

/celeb/actor/id: Get Detail of a particular actor. Only available if Celeb has acted in a movie.

# User Model
## Users of this site

/user: Post a new user

/user/username:

	Get: Details of this user

	Put: Update this user(Username cannot be changed). Partial changes allowed.

	Delete

```javascript
{
"username": "Slug-field",
"name": "Name",
"birth_date": "YYYY-MM-DD",
"email": "me@email.com"
}
```

# Movie Model

/movies:

	Get: List of all movies

	Post: Add new movies

/movies/id:

	Get: Detail of Specific Movie

	Put: Partial Update Movie(Cannot change Id)

	Delete

```javascript
{
"title": "Unique Title for Movie",
"description": "Required, Cannot be blank.",
"release_date": "YYYY-MM-DD",
"directors": [id1, id3, ...],
"actors": [id1, id3, ...]
}
```

/movies/rating/int

	Get: List movies with rating greater than int(0 - 10)

/movies/id/ratings:

	Get: List all ratings for a movie

	Post: Add a rating for movie

/movie/id/ratings/username:

	Get: Details of Rating for Movie: id by User: username

	Put: Update this Rating(Can change only remarks and rating)

	Delete

```javascript
{
"user": "username",
"remarks": "Cannot be blank...",
"rating": "4.5"(Choices: 0.5, 1, 1.5, ..., 10)
}
```
