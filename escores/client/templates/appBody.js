

matches = new Mongo.Collection("leagueoflegendsMatches");

Template.appBody.helpers({
	matches: function()
	{
		return matches.find({}, {sort: {dateTime: -1}});
	}
});
