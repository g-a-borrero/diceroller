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
		die = re.findall("((\d+)d(\d+))", text)
		if die == []:
			die = [("", 1, 20)]
		user_rolls = roll(int(die[0][1]), int(die[0][2]))
	templateData = {"result": user_rolls["sum"], "rolls": user_rolls["list"]}
	return render_template_string(main_page2, **templateData)

def roll(num, sides):
	rolls = [random.randint(1, sides) for i in range(num)]
	roll_sum = sum(rolls)
	return({"list": rolls, "sum": roll_sum})

if __name__ == '__main__':
    app.run()
