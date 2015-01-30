
/*
var testData = [{
	tournament: "NA LCS",
	dateTime: "1/24/15", 
	winnerId: "1",
	matchId: "123",
	maxGames: "1",
	blue: "1",
	red: "2",
	liveStream: "twitch.tv",
	polldaddyId: "3",
	games:"1",
	name:""

}];*/

matches = new Mongo.Collection("leagueoflegendsMatches");

Template.appBody.helpers({
	matches: function()
	{
		return matches.find();
	}
});
