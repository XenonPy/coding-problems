# I need extra credit on this so I am going to procedurally generate the data with random and then perform the challenge. Rich for looking good, time for benchmarks
import random
import time
from rich.prompt import IntPrompt
from rich.console import Console
from rich.progress import track
console = Console()

seeds = [1, 2, 3, 4] # seed 1: 0-50 seed 2: 50-65 seed 3: 65-80 seed 4: 80-100. Seeds assert academic competence 

benchmark_level = int(IntPrompt.ask("Please enter the number of students to benchmark", default="10")) # You can benchmark the script by choosing a custom or preset benchmark level
gradebook = {

}

start = time.time()

for i in track(range(1, benchmark_level + 1)):
    gradebook.update({str(i): {}})

def generate_dataset(): # ngl snake case is kind of ugly
    for student in range(1,benchmark_level + 1):
        seed = random.choice(seeds)
        for grades in range (1, 6):
            if seed == 1:
                grade = random.randint(0, 50)
            elif seed == 2:
                grade = random.randint(50, 65)
            elif seed == 3:
                grade = random.randint(65, 80)
            elif seed == 4:
                grade = random.randint(80, 100)
            else:
                print("ERROR! Determining grade using seed")
                exit()
            gradebook[f"{student}"][str(grades)] = grade # Here, we are setting each student a random grade that we previously determined using their random seed.


with console.status("Populating dataset...", spinner="bouncingBall"):
    generate_dataset() # calling function to populate our gradebook dict
console.print(gradebook)

average_grades = {

}
print("\n\n")
# Now we determine the averages by using basic math
for student in track(gradebook): # var name should be ok because of local function scope right?
    avg = 0
    for grade in gradebook[student]:
        avg += int(gradebook[student][grade]) # avg += grade?
    average_grades[student] = avg / 5

end = time.time()

console.print(average_grades)
console.print(f"\n Time to run: {end-start}")


