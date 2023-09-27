 void function ( Binder arg0 ) { 
  EventBus loc0 = new EventBus ( ) ; 
  AmbariEventPublisher loc1 = new AmbariEventPublisher ( ) ; 
  replaceEventBus ( AmbariEventPublisher . class , loc1 , loc0 ) ; 
  arg0 . bind ( AmbariEventPublisher . class ) . toInstance ( loc1 ) ; 
  } 
 "force the eventbus from ambarieventpublisher to be serialand synchronous . concode_field_sep PlaceHolder placeHolder concode_field_sep void registerAlertListeners concode_elem_sep EventBus synchronizeAlertEventPublisher concode_elem_sep void replaceEventBus concode_elem_sep void registerAmbariListeners