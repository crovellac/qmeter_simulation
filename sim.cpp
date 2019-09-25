
{
  double knob = 0.5;
  
  fMain = new TGMainFrame(gClient->GetRoot(),200,200);
  fEcanvas = new TRootEmbeddedCanvas("Ecanvas",fMain,200,200);
  fMain->AddFrame(fEcanvas,new TGLayoutHints(kLHintsExpandX |
                kLHintsExpandY, 10, 10, 10, 1));

  fHslider1 = new TGHSlider(fMain, 100, kSlider1 | kScaleBoth, NULL);
  
  //Displaying the frame
  fMain->MapSubwindows();
  fMain->Resize(fMain->GetDefaultSize());
  fMain->MapWindow();
  
}


void DrawPlot() {
  TF1 *f1 = new TF1("f1", "sin(x)",0,gRandom->Rndm()*10);
  f1->Draw();
  TCanvas *fCanvas = fEcanvas->GetCanvas();
  fCanvas->Update();
}
