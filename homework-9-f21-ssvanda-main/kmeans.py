import numpy as np
from cluster import createClusters
from point import makePointList


def kmeans(point_data, cluster_data):
    """Performs k-means clustering on points.

    Args:
      point_data: a k-by-d numpy array used for creating a list of Points.
      cluster_data: A k-by-d numpy array used for creating a list of Clusters.

    Returns:
      A list of clusters (with update centers) after peforming k-means
      clustering on the points initialized from point_data
    """
    # Fill in

    # 1. Make list of points using makePointList and point_data
    listOfPoints = makePointList(point_data)
    # 2. Make list of clusters using createClusters and cluster_data
    listOfClusters = createClusters(cluster_data)
    # 3. As long as points keep moving:
    pointsKeepMoving = True
    while (pointsKeepMoving  == True):
    #   A. Move every point to its closest cluster (use Point.closest and
    #     Point.moveToCluster)
    #     Hint: keep track here whether any point changed clusters by
    #           seeing if any moveToCluster call returns "True"
      for everypoint in listOfPoints:
        pointsKeepMoving = everypoint.moveToCluster(everypoint.closest(listOfClusters))
    #   B. Update the centers for each cluster (use Cluster.updateCenter)
      for centers in listOfClusters:
        centers.updateCenter()

    # 4. Return the list of clusters, with the centers in their final positions
    clusters = listOfClusters
    return clusters


if __name__ == "__main__":
    data = np.array(
        [[0.5, 2.5], [0.3, 4.5], [-0.5, 3], [0, 1.2], [10, -5], [11, -4.5], [8, -3]],
        dtype=float,
    )
    centers = np.array([[0, 0], [1, 1]], dtype=float)

    clusters = kmeans(data, centers)
    for c in clusters:
        c.printAllPoints()
