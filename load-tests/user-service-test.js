import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 },  // ramp up to 10 users
    { duration: '1m',  target: 50 },  // stay at 50 users
    { duration: '30s', target: 100 }, // spike to 100 users
    { duration: '30s', target: 0 },   // ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests under 500ms
    http_req_failed: ['rate<0.01'],   // less than 1% errors
  },
};

const BASE_URL = 'http://localhost:8001';

export default function () {
  // Health check
  const healthRes = http.get(`${BASE_URL}/health`);
  check(healthRes, {
    'health status is 200': (r) => r.status === 200,
    'health response is healthy': (r) => JSON.parse(r.body).status === 'healthy',
  });

  sleep(0.5);

  // Register user
  const registerRes = http.post(
    `${BASE_URL}/users/register`,
    JSON.stringify({
      email: `user_${Math.random().toString(36).substring(7)}@test.com`,
      username: `user_${Math.random().toString(36).substring(7)}`,
      password: 'testpassword123',
    }),
    { headers: { 'Content-Type': 'application/json' } }
  );

  check(registerRes, {
    'register status is 201': (r) => r.status === 201,
  });

  sleep(1);
}