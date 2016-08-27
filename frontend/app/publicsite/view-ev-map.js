'use strict';

(function () {
    ymaps.ready(function () {
        var container = getContainer('view-ev-map-ycontainer');
        var data = readData(container);

        var map = new ymaps.Map(container, data.config);

        var placemark = new ymaps.Placemark(data.position);
        map.geoObjects.add(placemark);
    });

    function getContainer(className) {
        var elements = document.getElementsByClassName(className);

        if (!elements || elements.lenght > 1) {
            throw 'nope or too much containers # ' + className;
        }

        return elements[0];
    }

    function readData(container) {
        function smartRead(attribute, value) {
            var data = this.getAttribute(attribute);
            if (data) {
                return data;
            } else if (value) {
                return value;
            } else {
                throw 'broken map data # ' + attribute;
            }
        }

        var positionLatitude = smartRead.call(container, 'data-place-latitude'),
            positionLongitude = smartRead.call(container, 'data-place-longitude');

        return {
            position: [
                positionLatitude,
                positionLongitude
            ],
            config: {
                center: [
                    smartRead.call(container, 'data-center-latitude', positionLatitude),
                    smartRead.call(container, 'data-center-longitude', positionLongitude)
                ],
                zoom: smartRead.call(container, 'data-zoom', 15),
            },
        };
    }
})();