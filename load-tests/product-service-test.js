import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 20 },
    { duration: '1m',  target: 100 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

const BASE_URL = 'http://localhost:8002';

export default function () {
  // Health check
  const healthRes = http.get(`${BASE_URL}/health`);
  check(healthRes, {
    'health status is 200': (r) => r.status === 200,
  });

  sleep(0.5);

  // Create product
  const createRes = http.post(
    `${BASE_URL}/products/`,
    JSON.stringify({
      name: `Product ${Math.random().toString(36).substring(7)}`,
      description: 'Test product',
      price: Math.random() * 100,
      stock: Math.floor(Math.random() * 100),
      category: 'electronics',
    }),
    { headers: { 'Content-Type': 'application/json' } }
  );

  check(createRes, {
    'create product status is 201': (r) => r.status === 201,
  });

  sleep(0.5);

  // List products
  const listRes = http.get(`${BASE_URL}/products/`);
  check(listRes, {
    'list products status is 200': (r) => r.status === 200,
  });

  sleep(1);
}