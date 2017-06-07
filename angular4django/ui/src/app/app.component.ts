import { Component } from '@angular/core';
import { RobotService } from './robot.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [RobotService]
})
export class AppComponent {

  constructor (private robotService: RobotService) {}
  title = 'app';
  result = '';
  terrain = '';

  submitClicked(terrain)
  {
    this.robotService.getPath(terrain).subscribe(
                     result => this.result = result,
                     error =>  this.result = <any>error)
  }
}
