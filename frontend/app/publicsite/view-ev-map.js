;(function (ymaps) {
    'use strict';

    ymaps.ready(function () {
        var container = getContainer('view-ev-map-ycontainer');
        var data = readData(container);

        var map = new ymaps.Map(container, data.config);

        var placemark = new ymaps.Placemark(
            data.position,
            {},
            data.icon
                ? {
                    iconLayout: 'default#image',
                    iconImageHref: data.icon,
                    iconImageSize: [30, 30],
                    iconImageOffset: [-15, -30],
                }
                : {
                    preset: 'twirl#blackDotIcon',
                }
        );
        map.geoObjects.add(placemark);

        function getContainer(className) {
            var elements = document.getElementsByClassName(className);

            if (!elements || elements.lenght > 1) {
                throw new Error('nope or too much containers # ' + className);
            }

            return elements[0];
        }

        function readData(container) {
            function smartRead(container, attribute, value, fail) {
                value = value || undefined;
                fail = fail || false;

                var data = container.getAttribute(attribute);
                if (data) {
                    return data;
                } else if (value) {
                    return value;
                } else if (!fail) {
                    return data;
                } else {
                    throw new Error('broken map data # ' + attribute);
                }
            }

            var positionLatitude = smartRead(container, 'data-place-latitude'),
                positionLongitude = smartRead(container, 'data-place-longitude');

            return {
                position: [
                    positionLatitude,
                    positionLongitude
                ],
                config: {
                    center: [
                        smartRead(container, 'data-center-latitude', positionLatitude),
                        smartRead(container, 'data-center-longitude', positionLongitude)
                    ],
                    zoom: smartRead(container, 'data-zoom', 15),
                },
                icon : smartRead(container, 'data-icon', null, false),
            };
        }
    });
})(ymaps);