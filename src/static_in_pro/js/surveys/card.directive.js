(function(){
	'use strict';

	angular.module('scrumboard.demo')
		.directive('scrumboardCard', CardDirective);

	function CardDirective(){
		return {
			templateUrl: 'surveys/question-template/',
			restrict: 'E',
			controller: ['$scope', '$http', function ($scope, $http){
				var url = '/scrumboard/cards/' + $scope.card.id + '/';
				$scope.update = function() {
					$http.put(
						url,
						$scope.card
					);
				};

				$scope.delete = function() {
					$http.delete(url).then(
						function(){
							var cards = $scope.list.cards;
							cards.splice(
								cards.indexOf($scope.card),
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