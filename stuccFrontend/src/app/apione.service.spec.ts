import { TestBed } from '@angular/core/testing';

import { ApioneService } from './apione.service';

describe('ApioneService', () => {
  let service: ApioneService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApioneService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
