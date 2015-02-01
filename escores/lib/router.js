
Router.configure({
  layoutTemplate: 'layout',
  //loadingTemplate: 'loading',
  waitOn: function() {Meteor.subscribe('matches')}
});
Router.route('/', {name: 'appBody'});
Router.route('/leaguematches/:matchId',{
	name: 'leaguematchPage',
	data: function() { return matches.findOne({matchId: this.params.matchId});}
});
Router.route('/leagueteams/:teamId',{
	name: 'leagueteamPage',
	data: function() {}
});