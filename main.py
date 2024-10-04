import os

def makeCommits(days: int):
    if days < 1:
        os.system('git push')
        return 0  # Return a value (0) when pushing is done
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!!\n')
        
        # staging 
        os.system('git add data.txt')

        # commit 
        os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

        # Continue with the next day
        makeCommits(days -6)  # No need to multiply, just call recursively

# Call the function
makeCommits(120)
