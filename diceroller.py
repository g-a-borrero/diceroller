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

main_page2 = re.sub("(Result:)", "\\1 {{ result }}", main_page)

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
		roll_sum = roll(int(die[0][1]), int(die[0][2]))
	templateData = {"result": roll_sum}
	return render_template_string(main_page2, **templateData)

def roll(num, sides, roll_sum=0):
	roll_sum += random.randint(1, sides)
	if num > 1:
		return(roll(num-1, sides, roll_sum))
	else:
		return(roll_sum)

if __name__ == '__main__':
    app.run()