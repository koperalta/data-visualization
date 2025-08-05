import plotly.express as px

from die import Die

# Three six-sided dice
die_1 = Die()
die_2 = Die()

# Roll two dice 1000 times and then adding the results
# _ means "we don't care about the value"
results = [die_1.roll() + die_2.roll() for _ in range(1000)]

# Analyze the results
poss_results = range(2, (die_1.num_sides + die_2.num_sides) + 1)
frequencies = [results.count(value) for value in poss_results]

# Prepare the title and labels for the plot
title = "Results of rolling two D6 1,000 times, then adding the results"
labels = {
    "x": "Result",
    "y": "Frequency",
}

# Visualize the results using Plotly
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Show the bar chart
# fig.show()

# Save the bar chart as an HTML file
fig.write_html("assets/die_visual_two_d6.html")