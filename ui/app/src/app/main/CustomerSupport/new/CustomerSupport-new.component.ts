import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CustomerSupport-new',
  templateUrl: './CustomerSupport-new.component.html',
  styleUrls: ['./CustomerSupport-new.component.scss']
})
export class CustomerSupportNewComponent {
  @ViewChild("CustomerSupportForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}