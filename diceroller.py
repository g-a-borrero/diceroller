from flask import Flask, request, render_template_string
app = Flask(__name__)
import random
import re

main_page = """
<html>
	<body>
		<form method="POST" action="/">
			<label for="diceString">Dice:</label>
			<input type="text" id="diceString" name="diceString" placeholder="1d20">
			<input type="submit" value="Submit"><br><br>
            <label>Result:</label>
		</form>
	</body>
</html>
"""

main_page2 = re.sub("(Result:)", "\\1 {{ result }} {{ rolls }}", main_page)

@app.route("/", methods=["GET"])
def index():
	return main_page

@app.route("/", methods=["GET", "POST"])
def diceRoller():
	if request.method == "POST":
		text = request.form.get("diceString").replace(" ", "")
		die = re.findall("(?:(\d+)d(\d+))", text)
		if die == []:
			die = [("", 1, 20)]
		user_rolls = roll(int(die[0][0]), int(die[0][1]))
		reroll = re.findall("r([ro])(\d+)", text)
		if reroll != [] and int(reroll[0][1]) <= int(die[0][1]) and int(die[0][1]) != 1:
			if reroll[0][0] == "o":
				# reroll the given number once for each time it shows up
				instances_of_number = [i for i, val in enumerate(user_rolls["list"]) if val == int(reroll[0][1])]
				instances_offset = 0
				for each_instance in instances_of_number:
					user_rolls["list"][each_instance+instances_offset] = reroll[0][1] + " (rerolled)"
					instances_offset +=1
					user_rolls["list"].insert(each_instance+instances_offset, roll(1, int(die[0][1]))["sum"])
				user_rolls["sum"] = sum([i if type(i) == int else 0 for i in user_rolls["list"]])
			else:				
				# reroll the given number every time it shows up
				pass
		# Keeping the highest or lowest rolls
		keep = re.findall("k([hl])(\d+)", text)
		if keep != [] and int(keep[0][1]) < int(die[0][1]):
			keep_list = [i for i in user_rolls["list"] if type(i) == int]
			keep_list.sort()
			if keep[0][0] == "h":				
				keep_list = keep_list[len(keep_list)-int(keep[0][1]):]
			else:
				keep_list = keep_list[:int(keep[0][1])]
			user_rolls["sum"] = str(sum(keep_list)) + " " + str(keep_list) + " ||"
		# sum([i if type(i) == int else 0 for i in a])

	templateData = {"result": user_rolls["sum"], "rolls": user_rolls["list"]}
	return render_template_string(main_page2, **templateData)

def roll(num, sides):
	rolls = [random.randint(1, sides) for i in range(num)]
	roll_sum = sum(rolls)
	return({"list": rolls, "sum": roll_sum})

if __name__ == '__main__':
    app.run()
