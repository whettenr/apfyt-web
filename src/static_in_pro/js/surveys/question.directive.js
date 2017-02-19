(function(){
	'use strict';

	angular.module('survey')
		.directive('surveyQuestion', QuestionDirective);

	function QuestionDirective(){
		return {
			templateUrl: '/static/html/question.html/',
			restrict: 'E',
			controller: ['$scope', '$http', function ($scope, $http){
				var url = '/surveys/questions_api/' + $scope.question.id + '/';
				$scope.update = function() {
					$http.put(
						url,
						$scope.question
					);
				};

				$scope.delete = function() {
					$http.delete(url).then(
						function(){
							var cards = $scope.survey.questions;
							questions.splice(
								questions.indexOf($scope.question),
								1
							);
						}
					);
				};

				$scope.modelOptions = {
					debounce: 500
				};
			}]
		}
	}
})();