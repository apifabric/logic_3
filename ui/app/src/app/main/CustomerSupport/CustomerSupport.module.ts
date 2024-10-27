import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CUSTOMERSUPPORT_MODULE_DECLARATIONS, CustomerSupportRoutingModule} from  './CustomerSupport-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CustomerSupportRoutingModule
  ],
  declarations: CUSTOMERSUPPORT_MODULE_DECLARATIONS,
  exports: CUSTOMERSUPPORT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CustomerSupportModule { }