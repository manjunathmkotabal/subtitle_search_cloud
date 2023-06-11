# subtitle_search_cloud
* its a microservices version of my (https://github.com/manjunathmkotabal/subtitle_search_monolith)
* Upload videos with embedded subtitles and search for vides with phrases

## Description

This project is a video search application that allows users to search for videos based on keyword queries. The application retrieves videos from an S3 bucket and provides a search interface where users can enter keywords. The application then queries subtitles associated with the videos to find matches for the given keywords.

## Getting Started

### Note: there is an error in this project which needs to be fixed , related to the subtitle extraction process.
### Dependencies

* Django , celery 
* Linux OS

### Installing

* git clone this repo and replace all aws creadential wherever necessary.


### Executing program


* How to run the program
* make sure that your docker-desktop(windows) is running , if in linux just check you have docker engine and docker-compose
* then run this command for building
```
sudo docker-compose build 
```
* then run using 
```
sudo docker-compose up
```
* or to do both in a single command use 
```
sudo docker-compose up --build
```
* then visit - (http://localhost:8000/) or (http://0.0.0.0:8000/)

## Help

* if you find any errors, feel free to contact me

## Authors

ex. Manjunath Kotabal 
ex. [@manjukotabal](https://twitter.com/manjukotabal)

## Version History

* 0.1
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [Priyanshu Gupta](https://www.youtube.com/@PriyanshuGuptaOfficial)
* [ecowiser](https://wiser.eco/)

