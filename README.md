# NFL Draft Results Predictor
***
### This project attempts to serve the following purposes:
* Serve as an introductory project for working with neural networks on real data.
* Show how additional relevant data can improve classifcation performance.
* Begin a series of projects to accomplish the above two tasks.

The overall problem we are aiming to face:
>The NFL draft is a highly publicized event that is constantly given hundreds if not thousands of projects every year in order to determine what successful college football players will be selected by which teams. We will attempt to use machine learning to try to predict where a player should be selected purely based on their combine metrics. This includes both body metrics (height and weight) as well as drill scores (40 yard dash, vertical jump, broad jump, 3 cone drill, and 20 yard shuttle). The name and position of the player is included as well as the year of their draft class.

The question then becomes: is this approach a good solution at predicting where players will be drafted?

The answer(s) to this question will be discussed at the end of the project, but solutions and improvements will be given in following iterations of the project.

***
### Infromation about the dataset
Credit: The dataset used for this project originally comes from [this kaggle repository.](https://www.kaggle.com/savvastj/nfl-combine-data)
The original dataset has been slightly altered for this project.

I am unable to say for certain, but it can be safely assumed that the original dataset was scraped from https://pro-football-reference.com. The date of collection of the data is April 26, 2018.

| Field Name | Description |
| ------ | ------ |
| Player | First and last name of the player |
| Pos | The position the player played at the time of the combine |
| Ht | Height of the player in inches |
| Wt | Weight of the player in pounds |
| Forty | Time of the players 40 yard dash in seconds |
| Vertical | Height of the players vertical jump in inches |
| BenchReps | Number of repetitions the player did of 225 pounds on the bench press |
| BroadJump | Length of the players broad jump in inches |
| Cone | Time of the players 3 cone drill in seconds |
| Shuttle | Time of the players 20-yard shuttle in seconds |
| Year | The year the player was drafted |
| AV | Approximate Value. This is a statistic computed by pro-football-reference. Learn more [here](https://www.sports-reference.com/blog/approximate-value/) |
| Team | Team that drafted the player |
| Round | The round the player was drafted |
| Pick | The selection in the draft (overall) that the player was selected |

##### Note: If any of the fields are missing (or -1 after being cleaned) this means the player did not participate in that drill. Missing data in Team, Round, and Pick means the player went undrafted.
***
### Set up instructions

- Coming soon!

***

