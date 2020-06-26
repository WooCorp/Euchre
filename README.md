# WooCorp's EuchreBot  
## The Future of Euchre  
  
>STILL IN PROGRESS  
>NOT READY FOR ACTUAL USE  
  
### A Brief Explanation of the Contents of this Repository  
**AllHands.txt**- all possible hands in Reduced Suit Form. This is not meant for any analysis use, it is merely for viewing all possible hands in an easy to read format.  
**AllScenarios.txt**- all possible initial situations, including Position, Top Card, and Cards in hand. This is in Reduced Suit Form converted to numeric values. This is intended for use in analysis.  
**EuchreProbability.exe**- to run this executable, it must be downloaded and placed in a folder with all of the CSV files located within the Calling folder. Then it can be run to determine the statistics surrounding any particular scenario.  
**GameLog.csv**- this file contains all the games recorded on euchrevolution.com. For use in conjuction with Statistics.py for updating score data and calculating rankings.  
**Sandbox.py**- this script simulates four euchrebots playing against each other. This is where the core of the logic can be found and easily displayed.  
>**Calling** Folder- this folder contains all of the simulated data. These CSV files are then used in determining the statistically best call in the first or second phase of the game.  
>**Standings** Folder- this folder contains several CSV files that contain the processed rankings for the individuals and leagues on euchrevolution.com  