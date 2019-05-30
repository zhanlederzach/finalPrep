import {Component, Input, OnInit} from '@angular/core';
import {deserializeITask, ITask, ITaskList} from "../shared/models/models";
import {ProviderService} from "../shared/services/provider.service";

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {

  @Input()
  task_list: ITaskList;

  // public name: any = '';
  tasks: ITask[];
  task: ITask;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.getTasks(this.task_list);
    this.task = {
      id: null,
      name: null,
      due_on: new Date(),
      created_at: new Date(),
      status: null,
    };
  }

  deleteTask(p: ITask) {
    this.provider.deleteTask(p).then(res=>{
      console.log(p.name+' deleted');
    });
    this.getTasks(this.task_list)
  }

  updateTask(p: ITask) {
    this.provider.updateTask(p).then(res=>{
      console.log(p.name+' updated');
      p=res;
    }).catch(err=>{
      console.log('error');
      console.log(err);
    });
  }

  getTasks(task_list: ITaskList){
    this.tasks = null;
    this.provider.getTasksOfTaskList(task_list.id).then(res => {
      this.tasks = null;
      setTimeout(() => {
        this.tasks = res.map(task => deserializeITask(task));
        console.log(this.tasks);
      }, 500);
    });
  }

  createTask() {
    console.log(this.task);
    this.provider.createTask(this.task_list, this.task).then(res => {
      this.task = {
        id: null,
        name: null,
        due_on: new Date(),
        created_at: new Date(),
        status: null,
      };
      this.tasks.push(res);
    });
  }

  toDate($event: any) {
    return new Date($event);
  }

  getType(elem: any) {
    if (elem instanceof Date)
      return "Date";
    return typeof elem;
  }
}
