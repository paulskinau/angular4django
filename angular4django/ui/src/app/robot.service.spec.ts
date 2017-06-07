import { TestBed, inject } from '@angular/core/testing';

import { RobotService } from './robot.service';

describe('RobotServicee', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [RobotService]
    });
  });

  it('should be created', inject([RobotService], (service: RobotService) => {
    expect(service).toBeTruthy();
  }));
});
