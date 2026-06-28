import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '1m',  target: 20 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<2000'],
    http_req_failed: ['rate<0.1'],
  },
};

export default function () {
  const services = [
    'http://localhost:8001/health',
    'http://localhost:8002/health',
    'http://localhost:8003/health',
    'http://localhost:8004/health',
  ];

  services.forEach((url) => {
    const res = http.get(url);
    check(res, {
      [`${url} is up`]: (r) => r.status === 200,
    });
    sleep(0.5);
  });

  sleep(2);
}