LolGames = new Mongo.Collection("leagueoflegendsMatches");

Template.match.helpers({

redImg: function()
{
	var img= IEWIN? new Image() : document.createElement('img');
    img.src= "na.lolesports.com"+this.red.logoURL;
    return img;
}
});