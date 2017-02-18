(function() {
	'use strict';

	angular.module('survey')
		.config(['$routeProvider', config])
		.run(['$http', run]);

	function config($routeProvider) {
		$routeProvider
			.when('/', {
				templateUrl:'/surveys/',
				controller: 'SurveyController'
			})
			.otherwise('/');
	}

	function run($http) {
		$http.defaults.xsrfHeaderName = 'X-CSRFToken';
		$http.defaults.xsrfCookieName = 'csrftoken';
	}
})();