def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals)
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1] = (merged[-1][0], max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def intersect_intervals(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        start_a, end_a = a[i]
        start_b, end_b = b[j]
        start = max(start_a, start_b)
        end = min(end_a, end_b)
        if start < end:
            result.append((start, end))
        if end_a < end_b:
            i += 1
        else:
            j += 1
    return result


def appearance(intervals: dict) -> int:
    lesson_start, lesson_end = intervals["lesson"]

    def to_pairs(lst):
        return list(zip(lst[::2], lst[1::2]))

    pupil = merge_intervals(
        [
            (max(start, lesson_start), min(end, lesson_end))
            for start, end in to_pairs(intervals["pupil"])
            if end > lesson_start and start < lesson_end
        ]
    )
    tutor = merge_intervals(
        [
            (max(start, lesson_start), min(end, lesson_end))
            for start, end in to_pairs(intervals["tutor"])
            if end > lesson_start and start < lesson_end
        ]
    )

    both = intersect_intervals(pupil, tutor)
    return sum(end - start for start, end in both)
