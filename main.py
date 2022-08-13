from runner import Voice_command_Runner

"""
    
this module is a voice command use to recognize speech from pc mic (or maybe any other mic that can be connecter to the pc...) 

get the text that exported from the mic and run the commands relative to the text if any exist.


commander for now and the command they can execute:



        ========================================================================================
        
        SPOTIFY: 

            spotify is ON by default
            
            commands:
                - 'next song' -> move to the next song
                - 'previous song' -> move to the previous song
                - 'play song' -> play the song (if not on...)
                - 'pause song' -> pause the song
                - 'stop song' -> stop the song (the same as above but can hear both voice command)
    
        ========================================================================================
        
        
        
        ========================================================================================
        
        GOOGLE:
            Google is ON by default
    
    
            command: 
                - 'google' + any words to search -> this command open up chrome page and search the words given in google
                - 'google it' -> open up chrome page and search whatever copy to clipboard by ctrl + c    
                             
        ========================================================================================
         
         
         
        ========================================================================================    
            
        CMD:
            CMD is OFF by default to enable it you need to voice command -> "enable command"
            
            command:
                - 'open new window' or 'open new windows' -> open a new chrome window
                    
                    
        ======================================================================================== 
        
        
        
        ========================================================================================
        
        TEXT:
            TEXT is ON by default.

            commands:
                - 'to file' + flowing talk to write to new file -> writing the text to a new file
                
        ========================================================================================
        
        
        
        ========================================================================================
        
        VOLUME:
            VOLUME is ON by default.
            
            commands:
                - 'volume up' -> volume up by 2
                - 'volume down' -> volume down by 2
        
        ========================================================================================
    
"""


####################### LOGGER ########################


    
def main():
    runner = Voice_command_Runner()
    runner.Run()
    
if __name__ == '__main__':
    main()
    
