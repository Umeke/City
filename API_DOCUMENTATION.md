# API Documentation

## Endpoints

### GET /api/products

Returns a list of products with their photos.

#### Headers

- `City-ID`: (optional) The ID of the city to filter the photos.

#### Response

- `200 OK`

```json
[
    {
        "id": 1,
        "name": "Product 1",
        "photos": [
            {
                "image": "/media/product_photos/photo1.jpg"
            },
            {
                "image": "/media/product_photos/photo2.jpg"
            }
        ]
    },
    {
        "id": 2,
        "name": "Product 2",
        "photos": [
            {
                "image": "/media/product_photos/photo3.jpg"
            }
        ]
    }
]
