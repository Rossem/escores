match_id = new Mongo.Collection("matchIds"); 
matches = new Mongo.Collection("leagueoflegendsMatches");

function getMatch() {

    var url = "http://na.lolesports.com:80/api/match/" + match_id.findOne({game: "leagueoflegends"}).id.toString() + ".json";
    console.log(url);
    var result = Meteor.http.get(url);
    var parsedData = JSON.parse(result.content);

    if (result.statusCode == 200) {
        if (parsedData['isFinished'] != '0') {
            var newId = match_id.findOne({game: "leagueoflegends"}).id + 1;
            match_id.update({game: "leagueoflegends"}, {$set:{id: newId}});
            matches.insert({
                tournament: parsedData['tournament'],
                dateTime: parsedData['dateTime'],
                winnerId: parsedData['winnerId'],
                matchId: parsedData['matchId'],
                maxGames: parsedData['maxGames'],
                blue: parsedData['contestants']['blue'],
                red: parsedData['contestants']['red'],
                liveStreams: parsedData['liveStreams'],
                polldaddyId: parsedData['polldaddyId'],
                games: parsedData['games'],
                name: parsedData['name']
            });
        }
    }
}


    
if (Meteor.isServer) {
   Meteor.setInterval(function() {getMatch();}, 60);
}
