import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ITaskList, ITask, IPost} from '../shared/models/models';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {

  public task_lists: ITaskList[] = [];
  public task_list: ITaskList;

  public tasks : ITask[] = [];
  public task : ITask;

  public loading = false;
  public name: any = '';

  public isLogged = false;
  public login = '';
  public password = '';

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    let token = localStorage.getItem("token")
    if(token){
      this.isLogged=true;
      this.getTaskLists();
    }
  }

  getTaskLists(){
    // this.task_lists = null;
    // this.provider.getContacts().then(res => {
    //   this.task_lists = res;
    //   setTimeout(() => {
    //     this.loading = true;
    //   }, 500);
    // });
  }

  updateTaskList(c: ITaskList) {
    this.provider.updateTaskList(c).then(res => {
      console.log(c.name + ' updated');
    });
  }

  deleteTaskList(c: ITaskList){
    this.provider.deleteTaskList(c).then(res => {
      console.log(c.name + ' deleted');
      this.getTaskLists();
    });
  }

  createTaskList(){
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.task_lists.push(res);
      });
    }
  }

  onPostClick(c: ITaskList) {
    this.task_list=null;
    setTimeout( ()=> {
      this.task_list=c;
    }, 200);

  }

  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        this.getTaskLists();
      });
    }
  }

  logout() {
    localStorage.clear();
    this.isLogged=false;
  }
}

