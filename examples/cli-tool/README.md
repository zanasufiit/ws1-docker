# Use docker for CLI tools

Using containers you can also get rid of most of the problems with CLI tools. For example, if you create a CLI application in python which has some dependencies you need to have them installed while using them. Some dependencies might be difficult to install (e.g. needs to be compiled) or take a long time.

Thanks to docker you can create simple one-off containers with CLI interface.

## Micro-curl
We prepared a simple application made with Python 3.8 using Click (for CLI) and requests libraries. All this application does is allowing us to do:

```bash
python micro-curl.py <url>
```

and it will print out the webpage content (or fail).

If we wanted to use this application normally we would need to have Click and requests installed in our python and if for some case exact python version was needed that would also have to be satisfied.

### *Docker to the rescue!*

We can make a docker image which will hide all these requirements.


As the first step, we need to create a [Dockerfile](app/Dockerfile) after that we can build an image.

```
docker build ./app -t znf/micro-curl:live
```

Now we have a new docker image in our local registry (?todo).
We can use this image to run one-off containers.
```
docker run --rm znf/micro-curl:live https://zanasufiit.sk/
```

The `--rm` flag means that the container will be deleted after it finishes its run.

### Push it
Now is only at your local machine but what if you want to use it at your server or wherever else? 

Push it to the registry!

```
docker tag znf/micro-curl:live zanasufiit/micro-curl
docker push zanasufiit/micro-curl
```

Now you can use this image anywhere by doing:

```
docker run --rm zanasufiit/micro-curl <url>
```