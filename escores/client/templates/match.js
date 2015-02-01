Template.match.helpers({

	blueColor: function() {
		var color = {
			win: "green",
			lose: "red"
		};
		if (this.winnerId == this.blue.id)
			return color.win;
		else if (this.winnerId == this.red.id)
			return color.lose;
	},

	blueWins: function() {
		var a = document.createElement("span");
		var text = "";

		if (this.winnerId == this.blue.id)
			text = document.createTextNode(this.maxGames.toString());
		else
			text = document.createTextNode("0");
		a.appendChild(text);
		return a.textContent;
	},

	redColor: function(){
		var color = {
			win: "green",
			lose: "red"
		};
		if(this.winnerId==this.red.id)
			return color.win;
		else if(this.winnerId ==this.blue.id)
			return color.lose;
	},
	redWins:function(){
		var a = document.createElement("span");
		var text = "";
		if(this.winnerId == this.red.id)
			text = document.createTextNode(this.maxGames.toString());
		else
		{
			/*var count = 0;
			var total = 0;
			while(count < this.maxGames-1)
			{

			}*/
			text = document.createTextNode("0");
		}
		a.appendChild(text);
		return a.textContent;
	}
});