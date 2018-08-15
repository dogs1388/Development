#Socialbox && matplot lib
import matplotlib.pyplot as plt
Greeting = "Hello, My name is Helsing"
print(Greeting)
name = input("What is your name? ")
print("Nice to meet you, " + name)
subject = input("What is your favourite subject? Chose from following: Maths, Ist, DT, English, history, Science ")

if subject == 'Maths' or 'IST':
	subjectMathsIst = input("Do you want to see my graph which i can generate for you? yes/no ")

	if subjectMathsIst == 'yes':
		graphChoice = input("Do you want to give me a data points or use existing spreadsheet? dataPoints/spreadsheet? ")

	if graphChoice == 'dataPoints':
				
				#asks for data
				xLabel = input("name for x label ")
				yLabel = input("name for y label ")
				plotx = input("Tell me 6 numbers for x axis ")
				ploty = input("tell me 6 numbers for y axis ")
				
				#converts str to array
				plotx = plotx.split(' ')
				ploty = ploty.split(' ')

				print(plotx)
				print(ploty)

				#plot the data
				plt.plot(plotx, ploty)
				plt.ylabel(yLabel)
				plt.xlabel(xLabel)
				plt.show

	if graphChoice == 'spreadsheet':
				plt.plot([1,2,3,4])
				plt.ylabel('nimbers')
				plt.show()
