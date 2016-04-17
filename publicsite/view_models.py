from datetime import datetime


def _read_full_points(points):
    return [PointVM(p) for p in points.select_related().prefetch_related('materials').all()]


class PointVM:
    def __init__(self, point):
        self.title = point.title
        self.description = point.description
        self.start = point.start
        end = datetime.combine(datetime.today(), point.start) + point.duration
        self.end = end.time()
        self.duration = point.duration
        self.authors = list(point.authors.all())
        self.materials = point.materials


class SectionVM:
    def __init__(self, section):
        self.name = section.name
        self.points = _read_full_points(section.points)


class EventVM:
    def __init__(self, event):
        self.name = event.name
        self.description = event.description
        self.date = event.date
        self.sections = [
            SectionVM(s) for s in event.sections.all()
        ]
        if self.sections and len(self.sections):
            self.points = [p for p in [s.points for s in self.sections]]
        else:
            self.points = _read_full_points(event.points)
        self.place = event.place
