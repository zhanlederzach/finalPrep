import {Component, OnInit} from '@angular/core';
import {ProviderService} from "../shared/services/provider.service";
import {IContact, IQuery, ITaskList} from "../shared/models/models";

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

  public isLogged = false;
  public login = '';
  public password = '';
  public contacts: IContact[] = [];
  public contact: IContact;
  public loading = false;
  public name: any = '';
  public phone: any = '';
  public allowed: false;
  public editable: number;
  query: string = '';

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    let token = localStorage.getItem("token")
    if (token) {
      this.isLogged = true;
      this.contact = {
        id: null,
        name: null,
        phone: null,
      };
      this.getContacts();
    }
  }

  getContacts(query?: IQuery) {
    this.contacts = null;
    this.provider.getContacts(query).then(res => {
      this.contacts = res;
      console.log(res);
      this.loading = false;
      setTimeout(() => {
        this.loading = true;
      }, 500);
    });
  }

  onContactClick(c: IContact) {
    this.provider.getContact(c).then(res => {
      this.contact = null;
      setTimeout(() => {
        this.contact = res;
        // for (let c of this.contacts) {
        //   if (c.id == this.contact.id) {
        //     c.my_or_not = this.contact.my_or_not;
        //   }
        // }
      }, 200);
    });
  }

  createContact() {
    if (this.name !== '' && this.phone !== '') {
      this.provider.createContact(this.name, this.phone).then(res => {
        this.name = '';
        this.phone = '';
        this.contacts.push(res);
      });
    }
  }

  updateContact(c: IContact) {
    this.editable = c.id;
  }

  deleteContact(c: IContact) {
    this.provider.deleteContact(c).then(res => {
      console.log(c.name + ' deleted');
      this.getContacts();
    });
  }

  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        this.getContacts();
      });
    }
  }

  logout() {
    localStorage.clear();
    this.isLogged = false;
  }

  onSaveClick(c: IContact) {
    console.log(c);
    this.provider.updateContact(c).then(res => {
      c = res;
      console.log(c.name + ' updated');
      this.editable = null;
    });
  }

  search(query: string) {
    this.getContacts({
      query: this.query});
  }

  sortByName() {
    this.getContacts({
      query: this.query,
      sort_by_name: true});
  }

  onlyMineFilter() {
    this.getContacts({
      query: this.query,
      only_mine: true});
  }
}
