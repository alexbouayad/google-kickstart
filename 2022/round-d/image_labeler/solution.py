from statistics import median


def max_metric(regions, n_categories):
    regions.sort()
    k = len(regions) - n_categories + 1
    min_regions = regions[:k]
    max_regions = regions[k:]
    return median(min_regions) + sum(max_regions)


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        _, n_categories = map(int, input().split())
        regions = list(map(int, input().split()))
        print(f"Case #{case}: {max_metric(regions, n_categories)}")
