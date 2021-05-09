using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Licht : MonoBehaviour
{
    public MeshRenderer lRenderer;
    public Material lOff;
    
    public Material lOn;
    public Light areaLight;
    public float intervalOn = 1f;
    public float intervalOff= 2f;
    private float timeToSwitch = 1f;
    private bool leuchten=false;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("l"))
        {
            leuchten = !leuchten;
                
        }

        if (leuchten)
        {
            if (timeToSwitch < 0)
            {
                if (areaLight.enabled)
                {
                    TurnOff();
                    timeToSwitch = intervalOff;
                }
                else
                {
                    TurnOn();
                    timeToSwitch = intervalOn;
                }
            }

            timeToSwitch -= Time.deltaTime;

        }else if(areaLight.enabled)
        {
            TurnOff();
        }
        
    }

    void TurnOff()
    {
        areaLight.enabled = false;
        lRenderer.material = lOff;

    }

    void TurnOn()
    {
        areaLight.enabled = true;
        lRenderer.material = lOn;
    }
}
